<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/streetview/publish/v1/rpcmessages.proto

namespace Google\Streetview\Publish\V1;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * <pre>
 * Response to batch delete of one or more photos.
 * </pre>
 *
 * Protobuf type <code>google.streetview.publish.v1.BatchDeletePhotosResponse</code>
 */
class BatchDeletePhotosResponse extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     * The status for the operation to delete a single photo in the batch request.
     * </pre>
     *
     * <code>repeated .google.rpc.Status status = 1;</code>
     */
    private $status;

    public function __construct() {
        \GPBMetadata\Google\Streetview\Publish\V1\Rpcmessages::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     * The status for the operation to delete a single photo in the batch request.
     * </pre>
     *
     * <code>repeated .google.rpc.Status status = 1;</code>
     */
    public function getStatus()
    {
        return $this->status;
    }

    /**
     * <pre>
     * The status for the operation to delete a single photo in the batch request.
     * </pre>
     *
     * <code>repeated .google.rpc.Status status = 1;</code>
     */
    public function setStatus(&$var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::MESSAGE, \Google\Rpc\Status::class);
        $this->status = $arr;
    }

}

